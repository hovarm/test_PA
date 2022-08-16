def numberOfBoomerangs(points):
        count = 0
        for i in range(len(points)):
            d = {}
            for j in range(len(points)):
                if i ==j:
                    continue
                dist = (points[i][0] - points[j][0])**2 + (points[i][1] -points[j][1])**2
                if dist in d.keys():
                    d[dist] =d[dist]+1
                else:
                    d[dist] =1
            for val in d.values():
                    count = count + val *(val-1)
        return count
