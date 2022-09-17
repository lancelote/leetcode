DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:
        aam, aad = [int(x) for x in aa.split("-")]
        alm, ald = [int(x) for x in la.split("-")]
        bam, bad = [int(x) for x in ab.split("-")]
        blm, bld = [int(x) for x in lb.split("-")]

        # no together interval
        if (alm, ald) < (bam, bad) or (blm, bld) < (aam, aad):
            return 0

        # start of together interval
        sm, sd = max((aam, aad), (bam, bad))

        # end of together interval
        em, ed = min((alm, ald), (blm, bld))

        # days in together interval
        days = sum(DAYS[m - 1] for m in range(sm, em + 1))
        days -= sd
        days -= DAYS[em - 1] - ed - 1

        return days
