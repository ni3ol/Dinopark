import datetime
import dateutil.parser
from string import ascii_uppercase

class ParkState(object):
    def __init__(self, maintenance_state, dino_state):
        self.maintenance_state = maintenance_state
        self.dino_state = dino_state
        self.park_state = {'time' : '', 'state' : {}}

    def build_park_state(self, time):
        # Convert string date to datetime format
        datetime = dateutil.parser.parse(time)
        maintenance_needed = False
        safe = True
        self.park_state['time'] = time
        # Create zone grid
        for i in ascii_uppercase:
            for j in range(15):
                zone = '{}{}'.format(i, j)
                if zone in self.maintenance_state:
                    maintenance_date = dateutil.parser.parse(self.maintenance_state[zone]['maintenance_performed'])
                    # Calculate if maintenance is due for zone
                    if (datetime - maintenance_date).days >= 30:
                        maintenance_needed = True
                if zone in self.dino_state['zones']:
                    # See if there are carnivores in zone
                    dinos = self.dino_state['zones'][zone]
                    for dino in dinos.values():
                        # Not safe if dinosaurs are not eating
                        if 'dino_fed' not in dino:
                            safe = False
                            break
                        else:
                            dino_fed = dateutil.parser.parse(dino['dino_fed'])
                            if (datetime - dino_fed).hours > int(dino['digestion_period_in_hours']):
                                safe = False
                                break
                self.park_state['state'][zone] = {'maintainence_due': maintenance_needed, 'safe': safe }
        return self.park_state
