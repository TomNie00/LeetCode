import collections


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """

        q = collections.deque()
        q.append(id)
        visited = [id]

        video_dict = collections.defaultdict()
        sol = []

        for i in range(level):
            size = len(q)
            while size:
                size -= 1
                curr_friend = q.popleft()
                for friend in friends[curr_friend]:
                    if friend not in visited:
                        visited.append(friend)
                        q.append(friend)

        while q:
            curr_friend = q.popleft()
            for video in watchedVideos[curr_friend]:
                if video not in video_dict:
                    video_dict[video] = 1
                else:
                    video_dict[video] += 1

        sol = [[key, value] for key, value in video_dict.items()]
        sol = sorted(sol, key=lambda x: (x[1], x[0]))

        return [x[0] for x in sol]

        # video_dict = dict(sorted(video_dict.items(), key=lambda item: (item[1], item[0])))
        # return [i for i in video_dict.keys()]


if __name__ == '__main__':
    object = Solution()
    watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
    friends = [[1, 2], [0, 3], [0, 3], [1, 2]]
    id = 0
    level = 1
    print(object.watchedVideosByFriends(watchedVideos, friends, id, level))
