# Challenge: Access Matrix

- **Level:** Intermediate
- **Category:** Authorization Logic
- **Estimated effort:** 20–25 minutes

## Scenario
A fictional training portal has these roles:

| Role | View course | Edit course | Manage users |
|---|---:|---:|---:|
| Learner | Yes | No | No |
| Trainer | Yes | Yes | No |
| Admin | Yes | Yes | Yes |

A Trainer attempts to manage users.

## Objective
Determine whether the action should be allowed under this role matrix.

## Hints
1. Check the requested action, not just whether the user is signed in.
2. Authentication and authorization are different.

## Solution
The action should be denied. The Trainer role has no permission to manage users.

Flag: `CYBERWOLF{deny_by_default}`

## Lesson
Enforce authorization server-side for every protected action and object. Hiding a button is not an access-control boundary.
