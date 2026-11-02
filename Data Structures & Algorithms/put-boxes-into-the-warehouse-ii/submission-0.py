class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        usable = [0] * n

        # tallest box that can reach room i from the left
        left_min = float('inf')
        for i in range(n):
            left_min = min(left_min, warehouse[i])
            usable[i] = left_min

        # from the right; keep whichever entrance allows the taller box
        right_min = float('inf')
        for i in range(n - 1, -1, -1):
            right_min = min(right_min, warehouse[i])
            usable[i] = max(usable[i], right_min)

        boxes = sorted(boxes)
        usable.sort()

        count = 0
        i = 0                        # smallest unplaced box
        for room in usable:          # rooms from shortest to tallest
            if i < len(boxes) and boxes[i] <= room:
                count += 1
                i += 1
            # otherwise this room is too short for every remaining box: skip it
        return count