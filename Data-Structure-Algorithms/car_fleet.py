
from typing import List
class CarFleet:
    """
    actually the fleet is the two cars met and then travel with same speed at reach the ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddtarget
    if the two cars reached the same time in target it also car fleet.
    """
    def check_carfleet(self,target:int,positions: List[int],speed_list: List[int]):
        #To compare a car can catch up another car using time
        time_tacking = [(position,(target-position)/speed) for position,speed in zip(positions,speed_list)]
        sorted_car_position=time_tacking.sort(reverse=True)
        prev_postion=None
        fleet_count=0
        for position in sorted_car_position:
            if not prev_postion:
                prev_postion=position[1]
                fleet_count+=1
                continue
            if position[1] > prev_postion:
                prev_postion=position[1]
                fleet_count+=1
        return fleet_count
            
            
    
target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]
totoal_car_fleets = CarFleet().check_carfleet(target,position,speed)
print(totoal_car_fleets)