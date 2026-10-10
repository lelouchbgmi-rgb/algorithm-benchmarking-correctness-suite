"""Repeatable local microbenchmark; timings are informational, not universal."""
import argparse, json, platform, random, statistics, sys, time
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from algolab.algorithms import binary_search
def linear_search(values,target):
    for i,value in enumerate(values):
        if value==target: return i
    return None
def measure(fn, values, queries):
    start=time.perf_counter()
    for q in queries: fn(values,q)
    return time.perf_counter()-start
def main():
    p=argparse.ArgumentParser(); p.add_argument('--size',type=int,default=50000); p.add_argument('--queries',type=int,default=2000); p.add_argument('--repeats',type=int,default=5); a=p.parse_args()
    if min(a.size,a.queries,a.repeats)<1: p.error('all arguments must be positive')
    rng=random.Random(20261010); values=list(range(0,a.size*2,2)); queries=[rng.randrange(a.size*2) for _ in range(a.queries)]; results={}
    for name,fn in [('binary_search',binary_search),('linear_search',linear_search)]:
        runs=[measure(fn,values,queries) for _ in range(a.repeats)]
        results[name]={'median_seconds':statistics.median(runs),'min_seconds':min(runs),'max_seconds':max(runs),'runs_seconds':runs}
    print(json.dumps({'python':sys.version.split()[0],'platform':platform.platform(),'seed':20261010,'input_size':a.size,'queries':a.queries,'results':results,'note':'Local microbenchmark; hardware and workload affect timings.'},indent=2))
if __name__=='__main__': main()
