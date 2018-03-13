#!/usr/bin/env python

import argparse
import networkx

def get_parser():
    parser = argparse.ArgumentParser(description="Convert shapefile to rnet format")
    parser.add_argument("shape_file")
    parser.add_argument("-o", "--out", metavar="OUTPUT", help="output dest (default: a.rnet)", default="a.rnet")
    return parser


def shp2rnet(args):
    graph = networkx.read_shp(args["shape_file"])
    edges = list(graph.edges)
    nodes = {}
    node_id = 0
    edge_id = 0

    with open(args["out"], 'w') as f_out:
        for edge in edges:
            from_lng = edge[0][0]
            from_lat = edge[0][1]
            to_lng = edge[1][0]
            to_lat = edge[1][1]
            from_key = str(from_lng) + "-" + str(from_lat)
            to_key = str(to_lng) + "-" + str(to_lat)
            if from_key not in nodes:
                nodes[from_key] = node_id
                node_id+=1
            if to_key not in nodes:
                nodes[to_key] = node_id
                node_id+=1
            from_id = nodes[from_key]
            to_id = nodes[to_key]
            row = "{} {} {} {} {} {} {}\n".format(edge_id, from_id, to_id,
                    from_lng, from_lat, to_lng, to_lat)
            f_out.write(row)
            edge_id+=1


if __name__ == "__main__":
    parser = get_parser()
    args = vars(parser.parse_args())
    shp2rnet(args)
