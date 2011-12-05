dzil_steps = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

dzil_steps['schedulers'] = []
dzil_steps['schedulers'].append(SingleBranchScheduler(
                            name="buildbot-dzil-steps-commit",
                            change_filter=filter.ChangeFilter(project='buildbot-dzil-steps'),
                            treeStableTimer=60,
                            builderNames=["buildbot-dzil-steps"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.python_twisted import Trial
from buildbot.config import BuilderConfig

factory_dzil = BuildFactory()
# check out the source
factory_dzil.addStep(Git(repourl='git://github.com/andrewrjones/buildbot-dzil-steps.git', mode='copy'))
# run the tests (note that this will require that 'trial' is installed)
factory_dzil.addStep(Trial(testpath=None, tests="test_steps_dzil.py"))

dzil_steps['builders'] = []
dzil_steps['builders'].append(
    BuilderConfig(name="buildbot-dzil-steps",
      slavenames=["mac", "l1"],
      factory=factory_dzil))
