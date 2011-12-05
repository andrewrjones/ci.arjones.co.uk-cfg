rake_steps = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

rake_steps['schedulers'] = []
rake_steps['schedulers'].append(SingleBranchScheduler(
                            name="buildbot-rake-steps-commit",
                            change_filter=filter.ChangeFilter(project='buildbot-rake-steps'),
                            treeStableTimer=60,
                            builderNames=["buildbot-rake-steps"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.python_twisted import Trial
from buildbot.config import BuilderConfig

factory_rake = BuildFactory()
# check out the source
factory_rake.addStep(Git(repourl='git://github.com/andrewrjones/buildbot-rake-steps.git', mode='copy'))
# run the tests (note that this will require that 'trial' is installed)
factory_rake.addStep(Trial(testpath=None, tests="test_steps_rake.py"))

rake_steps['builders'] = []
rake_steps['builders'].append(
    BuilderConfig(name="buildbot-rake-steps",
      slavenames=["l1"],
      factory=factory_rake))