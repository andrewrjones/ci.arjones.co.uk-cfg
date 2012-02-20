mp4meta = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

mp4meta['schedulers'] = []
mp4meta['schedulers'].append(SingleBranchScheduler(
                            name="App-MP4Meta-commit",
                            change_filter=filter.ChangeFilter(project='App-MP4Meta'),
                            treeStableTimer=60,
                            builderNames=["App-MP4Meta"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.dzil_steps.dzil import DzilAuthorDependencies, DzilDependencies, DzilSmoke

factory_mp4meta = BuildFactory()
# check out the source
factory_mp4meta.addStep(Git(repourl='git://github.com/andrewrjones/perl5-App-MP4Meta.git', mode='copy'))
# update deps
factory_mp4meta.addStep(DzilAuthorDependencies())
factory_mp4meta.addStep(DzilDependencies())
# run the tests
factory_mp4meta.addStep(DzilSmoke())

mp4meta['builders'] = []
mp4meta['builders'].append(
    BuilderConfig(name="App-MP4Meta",
      slavenames=["l1"],
      factory=factory_mp4meta))
