ant_task_sitemap = {}

####### SCHEDULERS

# Configure the Schedulers, which decide how to react to incoming changes.  In this

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.changes import filter

ant_task_sitemap['schedulers'] = []
ant_task_sitemap['schedulers'].append(SingleBranchScheduler(
                            name="ant-task-sitemap-commit",
                            change_filter=filter.ChangeFilter(project='ant-task-sitemap'),
                            treeStableTimer=60,
                            builderNames=["ant-task-sitemap"]))

####### BUILDERS

# The 'builders' list defines the Builders, which tell Buildbot how to perform a build:
# what steps, and which slaves can execute them.  Note that any particular build will
# only take place on one slave.

from buildbot.process.factory import BuildFactory
from buildbot.steps.source import Git
from buildbot.steps.shell import ShellCommand
from buildbot.config import BuilderConfig

from modules.ant_steps.ant import AntTest

ant_task_sitemap_factory = BuildFactory()
# check out the source
ant_task_sitemap_factory.addStep(Git(repourl='git://github.com/andrewrjones/ant-task-sitemap.git', mode='copy'))
# clean
ant_task_sitemap_factory.addStep(ShellCommand(command=["ant", "clean"]))
# run the tests
ant_task_sitemap_factory.addStep(AntTest())

ant_task_sitemap['builders'] = []
ant_task_sitemap['builders'].append(
    BuilderConfig(name="ant-task-sitemap",
      slavenames=["mac"],
      factory=ant_task_sitemap_factory))
