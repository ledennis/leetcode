# About
Solving leetcode problems and uploading the solutions here. The goal is to write a solution, notes, and to provide the space and time complexity.

## Useful Tips for Solving Problems
1. Will sorting help solve the problem?
2. Floyd's Cycle Detection Algorithm
   - Cycle Detection Phase: Use two pointers - a slow pointer that moves one step at a time and a fast pointer that moves two steps at a time. If a cycle exists, these pointers will eventually meet at some node within the cycle.
   - Cycle Start Detection Phase: Once a cycle is detected, reset one pointer to the head of the list while keeping the other at the meeting point. Move both pointers one step at a time. The node where they meet again is the start of the cycle.