ap = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

ap['schedulers'] = []
ap['schedulers'].append(SingleBranchScheduler(
                            name="AtomicParsley::Command-commit",
                            change_filter=filter.ChangeFilter(project='AtomicParsley::Command'),
                            treeStableTimer=60,
                            builderNames=["AtomicParsley::Command"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.dzil_steps.dzil import DzilAuthorDependencies, DzilDependencies, DzilSmoke

factory_ap = BuildFactory()
# check out the source
factory_ap.addStep(Git(repourl='git://github.com/andrewrjones/perl5-AtomicParsley-Command.git', mode='copy'))
# update deps
factory_dzil.addStep(DzilAuthorDependencies())
factory_dzil.addStep(DzilDependencies())
# run the tests
factory_dzil.addStep(DzilSmoke())

ap['builders'] = []
ap['builders'].append(
    BuilderConfig(name="AtomicParsley::Command",
      slavenames=["l1"],
      factory=factory_ap))
