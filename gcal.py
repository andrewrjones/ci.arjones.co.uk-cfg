gcal = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

gcal['schedulers'] = []
gcal['schedulers'].append(SingleBranchScheduler(
                            name="gcal-commit",
                            change_filter=filter.ChangeFilter(project='gcal'),
                            treeStableTimer=60,
                            builderNames=["gcal"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.dzil_steps.dzil import DzilAuthorDependencies, DzilDependencies, DzilSmokeVerbose

factory_gcal = BuildFactory()
# check out the source
factory_gcal.addStep(Git(repourl='git://github.com/andrewrjones/gcal.git', mode='copy'))
# update deps
factory_gcal.addStep(DzilAuthorDependencies())
factory_gcal.addStep(DzilDependencies())
# run the tests
factory_gcal.addStep(DzilSmokeVerbose())

gcal['builders'] = []
gcal['builders'].append(
    BuilderConfig(name="gcal",
      slavenames=["l1"],
      factory=factory_gcal))