# Nathaniel Burbine
# Daily Programmer Challenge 264 [Intermediate]
# https://www.reddit.com/r/dailyprogrammer/comments/4gqm90/20160427_challenge_264_intermediate_gossiping_bus/

class Driver:
    def __init__(self, route, initial_gossip):
        #print(route, initial_gossip)
        self.route = route
        self.stop_number = 0
        self.stop = self.route[self.stop_number]
        self.gossips = [initial_gossip]
        self.name = initial_gossip

    def gossip(self, new_gossips):
        self.gossips.extend(new_gossips)

    def next_stop(self):
        self.stop_number = (self.stop_number+1)%len(self.route)
        self.stop = self.route[self.stop_number]


def simulate(routes):
    drivers = []
    gossip = 0
    for route in routes:
        gossip += 1
        driver = Driver(route, gossip)
        drivers.append(driver)

    day = range(0, 480)
    # stop number -> gossips
    stations = dict()
    possible = False
    for minute in day:
        # Get each station's gossip
        for driver in drivers:
            gossips = stations.get(driver.stop, set())
            gossips.update(driver.gossips)
            stations[driver.stop] = gossips

        # Share the gossip at driver's station
        for driver in drivers:
            unheard_gossip = stations[driver.stop].difference(driver.gossips)
            driver.gossip(unheard_gossip)
            driver.next_stop()

        # Check if all drivers have all gossip
        all_gossip = True
        for driver in drivers:
            if len(driver.gossips) != gossip:
                all_gossip = False
                break

        if all_gossip:
            return minute

        stations.clear()

    if not possible:
        return 'never'


if __name__ == "__main__":
    example1 = "\
        3 1 2 3\
        3 2 3 1\
        4 2 3 4 5"
    example2 = "\
        2 1 2\
        5 2 8"
    challenge1 = "\
        7 11 2 2 4 8 2 2\
        3 0 11 8\
        5 11 8 10 3 11\
        5 9 2 5 0 3\
        7 4 8 2 8 1 0 5\
        3 6 8 9\
        4 2 11 3 3"
    challenge2 = '\
        12 23 15 2 8 20 21 3 23 3 27 20 0\
        21 14 8 20 10 0 23 3 24 23 0 19 14 12 10 9 12 12 11 6 27 5\
        8 18 27 10 11 22 29 23 14\
        13 7 14 1 9 14 16 12 0 10 13 19 16 17\
        24 25 21 4 6 19 1 3 26 11 22 28 14 14 27 7 20 8 7 4 1 8 10 18 21\
        13 20 26 22 6 5 6 23 26 2 21 16 26 24\
        6 7 17 2 22 23 21\
        23 14 22 28 10 23 7 21 3 20 24 23 8 8 21 13 15 6 9 17 27 17 13 14\
        23 13 1 15 5 16 7 26 22 29 17 3 14 16 16 18 6 10 3 14 10 17 27 25\
        25 28 5 21 8 10 27 21 23 28 7 20 6 6 9 29 27 26 24 3 12 10 21 10 12 17\
        26 22 26 13 10 19 3 15 2 3 25 29 25 19 19 24 1 26 22 10 17 19 28 11 22 2 13\
        8 4 25 15 20 9 11 3 19\
        24 29 4 17 2 0 8 19 11 28 13 4 16 5 15 25 16 5 6 1 0 19 7 4 6\
        16 25 15 17 20 27 1 11 1 18 14 23 27 25 26 17 1'

    inputs = [example1,example2,challenge1,challenge2]
    results = []
    for routes in inputs:
        routes = routes.split('        ')
        routes.pop(0)
        for route in routes:
            routes[routes.index(route)] = route.split(' ')

        results.append(simulate(routes))

    print(results)
