perl5_net_tvdb = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers import timed
from buildbot.changes import filter

perl5_net_tvdb['schedulers'] = []
perl5_net_tvdb['schedulers'].append(SingleBranchScheduler(
                            name="perl5-Net-TVDB-commit",
                            change_filter=filter.ChangeFilter(project='perl5-Net-TVDB'),
                            treeStableTimer=60,
                            builderNames=["perl5-Net-TVDB"]))
perl5_net_tvdb['schedulers'].append(
    timed.Nightly(name='perl5-Net-TVDB-nightly',
        builderNames=['perl5-Net-TVDB'],
        branch=None,
        hour=3,
        minute=0))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.dzil_steps.dzil import DzilAuthorDependencies, DzilDependencies, DzilSmoke

factory_dzil = BuildFactory()
# check out the source
factory_dzil.addStep(Git(repourl='git://github.com/andrewrjones/perl5-Net-TVDB.git', mode='copy'))
# update deps
factory_dzil.addStep(DzilAuthorDependencies())
factory_dzil.addStep(DzilDependencies())
# run the tests
factory_dzil.addStep(DzilSmoke())

perl5_net_tvdb['builders'] = []
perl5_net_tvdb['builders'].append(
    BuilderConfig(name="perl5-Net-TVDB",
      slavenames=["mac"],
      factory=factory_dzil))