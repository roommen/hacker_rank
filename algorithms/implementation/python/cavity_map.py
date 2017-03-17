n = int(input())
depth_map = [input() for _ in range(n)]

index_tracker = 1
cavity_map = list()
for depth in depth_map[1:-1]:
    prior_depth_list = depth_map[index_tracker - 1]
    post_depth_list = depth_map[index_tracker + 1]
    index_depth = 0
    for d in depth:
        if 0 < index_depth < n-1:
            if prior_depth_list[index_depth] != 'X' and post_depth_list[index_depth] != 'X' and depth[index_depth - 1] != 'X' and depth[index_depth + 1] != 'X':
                prior_depth_val = int(prior_depth_list[index_depth])
                post_depth_val = int(post_depth_list[index_depth])
                left_depth_val = int(depth[index_depth - 1])
                right_depth_val = int(depth[index_depth + 1])
                if int(d) > int(prior_depth_val) and int(d) > int(post_depth_val) and int(d) > int(left_depth_val) and int(d) > int(right_depth_val):
                    depth = depth[:index_depth] + 'X' + depth[index_depth+1:]
        index_depth += 1
    cavity_map.append(depth)
    index_tracker += 1

cavity_map.insert(0, depth_map[0])
if len(depth_map) > 1:
    cavity_map.append(depth_map[-1])

for cavity in cavity_map:
    print(cavity)
