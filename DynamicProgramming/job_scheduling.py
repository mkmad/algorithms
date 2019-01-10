class JobScheduling(object):

    """
    Given a list of jobs, with start time end time and the profit
    from executing the job. Find out how you would schedule these
    jobs so that no two jobs overlap and in turn maximizes the
    profit

    Sol:-

    First we sort the jobs in the increasing order of the end time,
    then we have two pointers i & j, where j traverses through the
    array just once and i goes from 0 to j - 1 each iteration.

    The goal is to see if:
        1) job at j does not overlap with job at i
        2) If it doesn't overlap, then value at array[j]
           is the max between the current value or the sum of
           the value at array[i] and the profit of the job at
           position j ( i.e. of value at j  and the
           value at i + profit of j)

           Note: value at i is already the best possible value
           at that position

    Also note: Two jobs are said to overlap if the end time at
               i is sightly lesser then the start time of job
               at j. If they are the same then its not an overlap
                     
    """

    def __init__(self, jobs):

        # sort the jobs according to end times
        self.jobs = sorted(jobs, key=lambda x: x[0][1])
        self.prices = []
        self.times = []
        for val in self.jobs:
            self.prices.append(val[1])
            self.times.append(val[0])

    def solution(self):
        for j in range(1, len(self.times)):
            for i in range(j):
                if self.times[j][0] >= self.times[i][1]:
                    self.prices[j] = max(
                        self.prices[j],
                        self.prices[i] + self.jobs[j][1]
                    )

        print self.prices


if __name__ == '__main__':
    # jobs is of the format ((start_time, end_time), profit)
    jobs_ = [
        ((7, 9), 2), ((5, 8), 11), ((6, 7), 4),
        ((4, 6), 5), ((2, 5), 6), ((1, 3), 5)
    ]
    j = JobScheduling(jobs_)
    j.solution()
