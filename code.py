class WeightedGraph:
    #initialization
    def __init__(self):
        self.cityList = {}

    def printGraph(self):
        #mengiterasi setiap city
        for city in self.cityList:
            #setiap kota print nama kota
            print(city, ":", self.cityList[city])

            # Print distances to neighboring cities
            for neighbor, distance in self.cityList[city].items():
                #print tetangga dan jarak
                print("    ->", neighbor, ":", distance)

    def tambahkanKota(self, kota):
        #jika kota tidak ada di cityList
        if kota not in self.cityList:
            #maka tambahkan kota
            self.cityList[kota] = {}
            return True
        return False

    def hapusKota(self, kotaDihapus):
        #jika kotaDihapus ada di cityList
        if kotaDihapus in self.cityList:
            # Remove the city from the city list
            del self.cityList[kotaDihapus]
            # Remove references to the deleted city from other cities
            for kota in self.cityList:
                #jika kotaDihapus ada di cityList[kota]
                if kotaDihapus in self.cityList[kota]:
                    #maka hapus kotaDihapus
                    del self.cityList[kota][kotaDihapus]
            return True
        return False

    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota1][kota2] = jarak
            self.cityList[kota2][kota1] = jarak
            return True
        return False

    def hapusJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            if kota2 in self.cityList[kota1]:
                del self.cityList[kota1][kota2]
                del self.cityList[kota2][kota1]
                return True
        return False

    def djikstra(self, source):
        # Initialize distances with infinity
        #distances = {city: float('inf') for city in self.cityList}
        
        distances = {}
        for city in self.cityList:
            distances[city] = float('inf')

distances[source] = 0
        print (distances)
        # Initialize list of unvisited cities
        unvisited_cities = []
        for city in self.cityList:
            unvisited_cities.append(city)
        #unvisited_cities = list(self.cityList.keys())
        print (unvisited_cities)

        while unvisited_cities:
            # Find the unvisited city with the smallest distance
            min_distance = float('inf')
            closest_city = None
            #mengiterasi setiap kota yang belum dikunjungi
            for city in unvisited_cities:
                #jika jarak kota lebih kecil dari min_distance
                if distances[city] < min_distance:
                    min_distance = distances[city]
                    closest_city = city

            # Remove the closest city from unvisited list
            unvisited_cities.remove(closest_city)

            # Update distances to neighboring cities
            for neighbor, weight in self.cityList[closest_city].items():
                #jika jarak kota terdekat + weight lebih kecil dari jarak kota tetangga
                distance = distances[closest_city] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance

        return distances
    

# Example usage with Dijkstra's algorithm:
petaIndonesia = WeightedGraph()
petaIndonesia.tambahkanKota("BANDUNG")
petaIndonesia.tambahkanKota("SUBANG")
petaIndonesia.tambahkanKota("INDRAMAYU")
petaIndonesia.tambahkanKota("CIREBON")
petaIndonesia.tambahkanKota("TEGAL")
petaIndonesia.tambahkanKota("PEMALANG")
petaIndonesia.tambahkanKota("PURWOKERTO")
petaIndonesia.tambahkanKota("CILACAP")
petaIndonesia.tambahkanKota("BANJAR")
petaIndonesia.tambahkanKota("TASIKMALAYA")
petaIndonesia.tambahkanKota("KUNINGAN")
petaIndonesia.tambahkanKota("SUMEDANG")

petaIndonesia.tambahkanJalan("BANDUNG","SUBANG", 53)
petaIndonesia.tambahkanJalan("BANDUNG","INDRAMAYU", 148)
petaIndonesia.tambahkanJalan("BANDUNG","CIREBON", 142)
petaIndonesia.tambahkanJalan("BANDUNG","TEGAL", 211)
petaIndonesia.tambahkanJalan("BANDUNG","PEMALANG", 257)
petaIndonesia.tambahkanJalan("BANDUNG","PURWOKERTO", 278)
petaIndonesia.tambahkanJalan("BANDUNG","CILACAP", 302)
petaIndonesia.tambahkanJalan("BANDUNG","BANJAR", 148)
petaIndonesia.tambahkanJalan("BANDUNG","TASIKMALAYA", 116)
petaIndonesia.tambahkanJalan("BANDUNG","KUNINGAN", 168)
petaIndonesia.tambahkanJalan("BANDUNG","SUMEDANG", 56)
petaIndonesia.tambahkanJalan("SUBANG","INDRAMAYU", 81)
petaIndonesia.tambahkanJalan("SUBANG","CIREBON", 131)
petaIndonesia.tambahkanJalan("SUBANG","TEGAL", 200)
petaIndonesia.tambahkanJalan("SUBANG","PEMALANG", 246)
petaIndonesia.tambahkanJalan("SUBANG","PURWOKERTO", 268)
petaIndonesia.tambahkanJalan("SUBANG","CILACAP", 291)
petaIndonesia.tambahkanJalan("SUBANG","BANJAR", 200)
petaIndonesia.tambahkanJalan("SUBANG","TASIKMALAYA", 184)
petaIndonesia.tambahkanJalan("SUBANG","KUNINGAN", 157)
petaIndonesia.tambahkanJalan("SUBANG","SUMEDANG", 112)
petaIndonesia.tambahkanJalan("INDRAMAYU","CIREBON", 55)
petaIndonesia.tambahkanJalan("INDRAMAYU","TEGAL", 134)
petaIndonesia.tambahkanJalan("INDRAMAYU","PEMALANG", 180)
petaIndonesia.tambahkanJalan("INDRAMAYU","PURWOKERTO", 201)
petaIndonesia.tambahkanJalan("INDRAMAYU","CILACAP", 225)
petaIndonesia.tambahkanJalan("INDRAMAYU","BANJAR", 159)
petaIndonesia.tambahkanJalan("INDRAMAYU","TASIKMALAYA", 146)
petaIndonesia.tambahkanJalan("INDRAMAYU","KUNINGAN", 91)
petaIndonesia.tambahkanJalan("INDRAMAYU","SUMEDANG", 94)
petaIndonesia.tambahkanJalan("CIREBON","TEGAL", 78 )
petaIndonesia.tambahkanJalan("CIREBON","PEMALANG", 125)
petaIndonesia.tambahkanJalan("CIREBON","PURWOKERTO", 146)
petaIndonesia.tambahkanJalan("CIREBON","CILACAP", 170)
petaIndonesia.tambahkanJalan("CIREBON","BANJAR", 103)
petaIndonesia.tambahkanJalan("CIREBON","TASIKMALAYA", 108)
petaIndonesia.tambahkanJalan("CIREBON","KUNINGAN", 35)
petaIndonesia.tambahkanJalan("CIREBON","SUMEDANG", 95)
petaIndonesia.tambahkanJalan("TEGAL","PEMALANG", 33)
petaIndonesia.tambahkanJalan("TEGAL","PURWOKERTO", 105)
petaIndonesia.tambahkanJalan("TEGAL","CILACAP", 129)
petaIndonesia.tambahkanJalan("TEGAL","BANJAR", 128)
petaIndonesia.tambahkanJalan("TEGAL","TASIKMALAYA", 177)
petaIndonesia.tambahkanJalan("TEGAL","KUNINGAN", 103)
petaIndonesia.tambahkanJalan("TEGAL","SUMEDANG", 162)
petaIndonesia.tambahkanJalan("PEMALANG","PURWOKERTO", 85)
petaIndonesia.tambahkanJalan("PEMALANG","CILACAP", 135)
petaIndonesia.tambahkanJalan("PEMALANG","BANJAR", 172)
petaIndonesia.tambahkanJalan("PEMALANG","TASIKMALAYA", 223)
petaIndonesia.tambahkanJalan("PEMALANG","KUNINGAN", 148)
petaIndonesia.tambahkanJalan("PEMALANG","SUMEDANG", 209)
petaIndonesia.tambahkanJalan("PURWOKERTO","CILACAP", 51)
petaIndonesia.tambahkanJalan("PURWOKERTO","BANJAR", 101)
petaIndonesia.tambahkanJalan("PURWOKERTO","TASIKMALAYA", 144)
petaIndonesia.tambahkanJalan("PURWOKERTO","KUNINGAN", 173)
petaIndonesia.tambahkanJalan("PURWOKERTO","SUMEDANG", 232)
petaIndonesia.tambahkanJalan("CILACAP","BANJAR", 107)
petaIndonesia.tambahkanJalan("CILACAP","TASIKMALAYA", 151)
petaIndonesia.tambahkanJalan("CILACAP","KUNINGAN", 151)
petaIndonesia.tambahkanJalan("CILACAP","SUMEDANG", 253)
petaIndonesia.tambahkanJalan("BANJAR","TASIKMALAYA", 43)
petaIndonesia.tambahkanJalan("BANJAR","KUNINGAN", 73)
petaIndonesia.tambahkanJalan("BANJAR","SUMEDANG", 124)
petaIndonesia.tambahkanJalan("TASIKMALAYA","KUNINGAN", 80)
petaIndonesia.tambahkanJalan("TASIKMALAYA","SUMEDANG", 92)
petaIndonesia.tambahkanJalan("SUMEDANG","KUNINGAN", 120)


petaIndonesia.printGraph()
shortest_distances = petaIndonesia.djikstra("BANDUNG")
print("Jarak terpendek dari Bandung ke kota lain:")
for city, distance in shortest_distances.items():
    print(city, ":", distance, "km")
