Title: Search2
Slug: search2
Date: 2015-04-02
Status: draft

In the field of AI, searcb is about coming up with a sequence of actions that achieves your goal.

A **Search problem** consists of:
- A state space - ways the world can be inside a model.
- A successor function(with actions, costs) - which actions are available for each state, and how will they change the world(to which state will I be taken to), and how much this action costs
- A start state, and the goal test

A **solution** is a sequence of actions(plan) which transforms the start state to a goal state.

Model -

Example: arad/bugharest.

Types of search:
Uninformed search
- Depth-first search
- Breadth-first search
- Uniform-cost search
Informed search.
- Heuristics
  - Admissibility
	Heuristic has to be cheaper than the actual cost to the goal.
  - Consistency
	Every arc's heuristic cost should be cheaper than a real cost.
	Change in a heuristic vs actual cost
- Greedy search
- A*
Graph Search


Pathing.

State graphs and search trees.
graphs witht infinite cycles. states occur only once.

8 puzzle....
