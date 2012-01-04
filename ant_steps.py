ant_steps = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

ant_steps['schedulers'] = []
ant_steps['schedulers'].append(SingleBranchScheduler(
                            name="buildbot-ant-steps-commit",
                            change_filter=filter.ChangeFilter(project='buildbot-ant-steps'),
                            treeStableTimer=60,
                            builderNames=["buildbot-ant-steps"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.python_twisted import Trial
from buildbot.config import BuilderConfig

factory_ant = BuildFactory()
# check out the source
factory_ant.addStep(Git(repourl='git://github.com/andrewrjones/buildbot-ant-steps.git', mode='copy'))
# run the tests (note that this will require that 'trial' is installed)
factory_ant.addStep(Trial(testpath=None, tests="test_steps_ant.py"))

ant_steps['builders'] = []
ant_steps['builders'].append(
    BuilderConfig(name="buildbot-ant-steps",
      slavenames=["mac"],
      factory=factory_ant))
