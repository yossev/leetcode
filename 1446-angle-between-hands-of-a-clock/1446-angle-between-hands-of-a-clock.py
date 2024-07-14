class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle_mins = 6 * minutes
        hour = hour % 12 
        angle_hours = (30 * hour) + (0.5 * minutes)


        angle = abs(angle_hours - angle_mins)
        smallest_angle = min(angle, 360 - angle)

        return smallest_angle