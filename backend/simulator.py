from park_state import ParkState

class Simulator(object):

    def __init__(self):
        self.dinos = {}
        self.park_maintenance_state = []
        self.dino_state = []
        self.events = []

    def handle(self, event):
        # Add event to list of all events
        self.events.append(event)
        # Build state of park as of current event
        self.handle_state(event)

    def handle_state(self, event):
        if event['kind'] == 'maintenance_performed':
            self.update_maintenance_state(event)

        if event['kind'] == 'dino_added' and event['herbivore'] is False:
            self.add_dino(event)

        if event['kind'] == 'dino_removed' and str(event['dinosaur_id']) in self.dinos:
            self.remove_dino(event)

        if event['kind'] == 'dino_location_updated' and str(event['dinosaur_id']) in self.dinos:
            self.update_dino_location(event)

        if event['kind'] == 'dino_fed' and str(event['dinosaur_id']) in self.dinos:
            self.update_dino_fed(event)

    def update_maintenance_state(self, event):
        if self.park_maintenance_state:
            # Create new state
            state = self.park_maintenance_state[-1].copy()
            state['time'] = event['time']
            state[event['location']] = {'maintenance_performed': event['time']}
            self.park_maintenance_state.append(state)
        else:
            state = {'time': event['time'], event['location']: {'maintenance_performed': event['time']}}
            self.park_maintenance_state.append(state)

    def add_dino(self, event):
        # Only store dinosaurs that are carnivores
        self.dinos[str(event['id'])] = event['digestion_period_in_hours']

    def remove_dino(self, event):
        dino_id = str(event['dinosaur_id'])
        # Remove dinosaur from park
        del self.dinos[dino_id]
        if self.dino_state:
            state = self.dino_state[-1].copy()
            state['time'] = event['time']
            for zone in state['zones'].values():
                # Remove dinosaur from zones if removed from park
                if dino_id in zone:
                    del zone[dino_id]
            self.dino_state.append(state)

    def update_dino_location(self, event):
        dino_id = str(event['dinosaur_id'])
        digestion_period_in_hours = self.dinos[dino_id]
        if self.dino_state:
            state = self.dino_state[-1].copy()
            state['time'] = event['time']
            # Add dinosaur to zone
            if state['zones'][event['location']]:
                zone = state['zones'][event['location']]
                zone[dino_id] = {'digestion_period_in_hours': digestion_period_in_hours}
            else:
                state['zones'][event['location']] = {dino_id: {'digestion_period_in_hours': digestion_period_in_hours}}
            for zone, dinos in last_dino_state['zones'].items():
                # Remove dinosaur from previous location
                if zone != event['location'] and dino_id in dinos:
                    del dinos[dino_id]
            self.dino_state.append(state)
        else:
            self.dino_state.append(
                {
                    'time': event['time'],
                    'zones' : {
                        event['location']:
                            {
                                dino_id: {'digestion_period_in_hours': digestion_period_in_hours}
                            }
                    }
                }
            )

    def update_dino_fed(self, event):
        dino_id = str(event['dinosaur_id'])
        if self.dino_state:
            state = self.dino_state[-1].copy()
            state['time'] = event['time']
            for zone in state['zones'].values():
                if dino_id in zone:
                    zone[dino_id]['dino_fed'] = event['time']
            self.dino_state.append(state)

    def get_park_state(self, time):
        # Use last state to calculate final park state
        park = ParkState(self.park_maintenance_state[-1], self.dino_state[-1])
        return park.build_park_state(time)
