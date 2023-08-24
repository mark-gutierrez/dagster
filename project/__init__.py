

# from dagster import ScheduleDefinition
# from hello import diamond
from dagster import get_dagster_logger, job, op, ScheduleDefinition, Definitions
# from hello import basic_schedule


@op
def array():
    return [1, 2, 3, 4, 5]


@op
def double(num):
    doubled = num * 2
    get_dagster_logger().info(f'{num} doubled is {doubled}')
    return doubled


@op
def for_loop(array):
    result = []
    for num in array:
        result.append(double(num))
    return result


@job
def diamond():
    results = for_loop(array())


basic_schedule = ScheduleDefinition(job=diamond, cron_schedule="* * * * *")

defs = Definitions(
    # Addition: add the job to Definitions object (see below)
    schedules=[basic_schedule],
)
