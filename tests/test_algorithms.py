import random
import pytest
from algolab.algorithms import binary_search, two_sum, bfs_shortest_path

def test_binary_search_boundaries_and_missing():
    a=[-9,-2,0,4,8,15]
    assert binary_search(a,-9)==0 and binary_search(a,15)==5
    assert binary_search(a,3) is None and binary_search([],3) is None

def test_binary_search_duplicates():
    a=[1,2,2,2,9]; i=binary_search(a,2)
    assert i is not None and a[i]==2

def test_two_sum_cases():
    assert two_sum([3,3],6)==(0,1)
    assert two_sum([-4,7,2],3)==(0,1)
    assert two_sum([1,2],8) is None and two_sum([],0) is None

def test_bfs_shortest_and_missing():
    g={"A":["B","C"],"B":["D"],"C":["D"],"D":[]}
    assert bfs_shortest_path(g,"A","D") in (["A","B","D"],["A","C","D"])
    assert bfs_shortest_path(g,"A","Z") is None
    assert bfs_shortest_path({},"X","X")==["X"]

def test_bfs_rejects_invalid_nodes():
    with pytest.raises(ValueError): bfs_shortest_path({},1,"x")
    with pytest.raises(ValueError): bfs_shortest_path({"a":[1]},"a","b")

def test_two_sum_randomized_against_reference():
    rng=random.Random(20261010)
    for _ in range(250):
        a=[rng.randint(-15,15) for _ in range(rng.randint(0,20))]; target=rng.randint(-20,20)
        result=two_sum(a,target)
        reference=next(((i,j) for i in range(len(a)) for j in range(i+1,len(a)) if a[i]+a[j]==target),None)
        if result is None: assert reference is None
        else: assert result[0]<result[1] and a[result[0]]+a[result[1]]==target

def test_binary_search_randomized():
    rng=random.Random(73)
    for _ in range(250):
        a=sorted(rng.randint(-100,100) for _ in range(rng.randint(0,80))); target=rng.randint(-110,110)
        i=binary_search(a,target); assert (i is not None)==(target in a)
        if i is not None: assert a[i]==target
