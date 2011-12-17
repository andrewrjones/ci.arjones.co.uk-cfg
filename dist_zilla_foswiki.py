dist_zilla_foswiki = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

dist_zilla_foswiki['schedulers'] = []
dist_zilla_foswiki['schedulers'].append(SingleBranchScheduler(
                            name="Dist-Zilla-Foswiki-commit",
                            change_filter=filter.ChangeFilter(project='Dist-Zilla-Foswiki'),
                            treeStableTimer=60,
                            builderNames=["Dist-Zilla-Foswiki"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.dzil_steps.dzil import DzilSmoke

factory_dzil = BuildFactory()
# check out the source
factory_dzil.addStep(Git(repourl='git://github.com/andrewrjones/Dist-Zilla-Foswiki.git', mode='copy'))
# update deps
factory_dzil.addStep(ShellCommand(command="dzil authordeps | cpanm"))
factory_dzil.addStep(ShellCommand(command="dzil listdeps | cpanm"))
# run the tests
factory_dzil.addStep(DzilSmoke())

dist_zilla_foswiki['builders'] = []
dist_zilla_foswiki['builders'].append(
    BuilderConfig(name="Dist-Zilla-Foswiki",
      slavenames=["l1"],
      factory=factory_dzil))
