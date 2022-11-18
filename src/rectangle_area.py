class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        area1 = abs(ax2 - ax1) * abs(ay2 - ay1)
        area2 = abs(bx2 - bx1) * abs(by2 - by1)

        common = 0

        if not (bx1 >= ax2 or by2 <= ay1 or bx2 <= ax1 or by1 >= ay2):
            cw = min(ax2, bx2) - max(ax1, bx1)
            ch = min(ay2, by2) - max(ay1, by1)
            common = cw * ch

        return area1 + area2 - common
