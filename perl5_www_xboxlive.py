perl5_www_xboxlive = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers import timed
from buildbot.changes import filter

perl5_www_xboxlive['schedulers'] = []
perl5_www_xboxlive['schedulers'].append(SingleBranchScheduler(
                            name="perl5-WWW-XBoxLive-commit",
                            change_filter=filter.ChangeFilter(project='perl5-WWW-XBoxLive'),
                            treeStableTimer=60,
                            builderNames=["perl5-WWW-XBoxLive"]))
perl5_www_xboxlive['schedulers'].append(
    timed.Nightly(name='perl5-WWW-XBoxLive-nightly',
        builderNames=['perl5-WWW-XBoxLive'],
        branch=None,
        hour=2,
        minute=0))

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
factory_dzil.addStep(Git(repourl='git://github.com/andrewrjones/perl5-WWW-XBoxLive.git', mode='copy'))
# update deps
factory_dzil.addStep(ShellCommand(command="dzil authordeps | cpanm"))
factory_dzil.addStep(ShellCommand(command="dzil listdeps | cpanm"))
# run the tests
factory_dzil.addStep(DzilSmoke())

perl5_www_xboxlive['builders'] = []
perl5_www_xboxlive['builders'].append(
    BuilderConfig(name="perl5-WWW-XBoxLive",
      slavenames=["mac"],
      factory=factory_dzil))