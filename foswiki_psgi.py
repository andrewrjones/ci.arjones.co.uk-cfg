foswiki_psgi = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

foswiki_psgi['schedulers'] = []
foswiki_psgi['schedulers'].append(SingleBranchScheduler(
                            name="foswiki-psgi-commit",
                            change_filter=filter.ChangeFilter(project='foswiki-psgi'),
                            treeStableTimer=60,
                            builderNames=["foswiki-psgi"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

factory_foswiki_psgi = BuildFactory()
# check out the source
factory_foswiki_psgi.addStep(Git(repourl='git://github.com/andrewrjones/foswiki', mode='copy'))
factory_foswiki_psgi.addStep(ShellCommand(command="cd core/test/unit; perl ../bin/TestRunner.pl -clean FoswikiSuite.pm"))

foswiki_psgi['builders'] = []
foswiki_psgi['builders'].append(
    BuilderConfig(name="foswiki-psgi",
      slavenames=["mac"],
      factory=factory_foswiki_psgi))
