ruby_ddg = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers import timed
from buildbot.changes import filter

ruby_ddg['schedulers'] = []
ruby_ddg['schedulers'].append(SingleBranchScheduler(
                            name="ruby-duck-duck-go-commit",
                            change_filter=filter.ChangeFilter(project='ruby-duck-duck-go'),
                            treeStableTimer=None,
                            builderNames=["ruby-duck-duck-go"]))
ruby_ddg['schedulers'].append(
    timed.Nightly(name='ruby-duck-duck-go-nightly',
        builderNames=['ruby-duck-duck-go'],
        branch=None,
        hour=4,
        minute=0))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
#from rake import RakeTest
from buildbot.config import BuilderConfig

factory_ddg = BuildFactory()
# check out the source
factory_ddg.addStep(Git(repourl='git://github.com/andrewrjones/ruby-duck-duck-go.git', mode='copy'))
# run the tests
#factory_ddg.addStep(RakeTest())
#factory_ddg.addStep(
#  ShellCommand(
#    command=["rake", "test"],
#    description=["testing"],
#    descriptionDone=["tests"]))

ruby_ddg['builders'] = []
ruby_ddg['builders'].append(
    BuilderConfig(name="ruby-duck-duck-go",
      slavenames=["l1"],
      factory=factory_ddg))