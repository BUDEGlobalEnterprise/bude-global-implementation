# Energy Point Rules: Gamifying Productivity & Recognition

## What Are Energy Points?

**Energy Points** are a built-in gamification system in ERPNext. Think of them as a "karma" or "points" system that automatically rewards users for performing actions within the system. This could be for creating documents, completing tasks, achieving sales targets, or even helping colleagues.

## Why Are They Important for Your Organization?

| Benefit | Description |
| :--- | :--- |
| **✅ Increased Adoption** | Makes using the system more engaging and rewarding, encouraging consistent use. |
| **✅ Recognizes Effort** | Provides instant, public recognition for work that might otherwise go unnoticed. |
| **✅ Promotes Best Practices** | You can reward actions that align with company goals (e.g., timely project closure, submitting expenses on time). |
| **✅ Drives Productivity** | Creates a healthy sense of competition and motivation to complete tasks. |
| **✅ Improves Data Quality** | Reward users for adding complete information, leading to better quality data in your system. |
| **✅ Enhances Collaboration** | Points can be given for helping others (e.g., solving a ticket, answering a question), fostering a team culture. |

---

## How Can My Org Use Energy Point Rules? (Practical Examples)

You can create rules to award points for almost any activity. Here are categorized examples:

### 1. For Sales & CRM
```python
Rule: "Closed-Won Deal"
-> When: `Sales Order` document is `Submitted`
-> Condition: `status` is `"Completed"`
-> Points: `+10` to the owner
```
```python
Rule: "New Lead Generator"
-> When: `Lead` document is `Submitted`
-> Points: `+5` to the owner
```

### 2. For Project Management
```python
Rule: "Task Champion"
-> When: `Task` document changes to `"Completed"` status
-> Points: `+5` to the user who closed it
```
```python
Rule: "On-Time Project"
-> When: `Project` status changes to `"Completed"`
-> Condition: `expected_end_date` >= `end_date` (finished on or before deadline)
-> Points: `+20` to the project manager
```

### 3. For Support & Helpdesk
```python
Rule: "Support Hero"
-> When: `Issue` status changes to `"Closed"`
-> Points: `+7` to the resolver
```
```python
Rule: "Customer Praise"
-> When: `Communication` is linked to an `Issue`
-> Condition: `sentiment` is `"Positive"`
-> Points: `+15` to the support agent
```

### 4. For HR & Operations
```python
Rule: "Expense Guru"
-> When: `Expense Claim` is `Submitted` (on-time)
-> Condition: `posting_date` is within the month
-> Points: `+3` to the employee
```
```python
Rule: "Attendance Star"
-> When: `Attendance` is `"Present"`
-> Condition: `last_attendance_date` was also `"Present"`
-> Points: `+1` for a perfect week
```

### 5. For General Best Practices
```python
Rule: "Early Bird"
-> When: Any assigned `ToDo` is closed
-> Condition: `date` is before `due_date`
-> Points: `+2` points
```
```python
Rule: "Knowledge Sharer"
-> When: A new `Article` in the Knowledge Base is published
-> Points: `+10` to the author
```

---

## How to Set Up Energy Point Rules

1.  Go to: **`Settings > Energy Point Rule > New`**
2.  **Reference Document:** Select the doctype you want to track (e.g., `Task`, `Sales Order`).
3.  **For Document Events:** Choose the trigger (`New`, `Submit`, `Cancel`, `Value Change`).
4.  **Condition (Optional):** Write a rule for when points should be awarded (e.g., `doc.status == "Completed"`).
5.  **Point Allocation:** Assign points to the `Owner`, `Assigned By`, a specific `User`, or a `Role`.
6.  **Save and Enable.** The rule is now active!

## Pro Tips & Best Practices

*   **Start Small:** Begin with 3-5 rules for key business processes. Don't overwhelm users.
*   **Balance the Points:** The points should reflect the effort and impact of the action. Closing a deal should be worth more than creating a lead.
*   **Promote the System:** Announce the launch, explain the rules, and maybe even link points to small monthly rewards (e.g., gift cards, company swag, executive recognition).
*   **Review and Adapt:** Check the **"Energy Point Leaderboard"** regularly. See what's working and adjust your rules to encourage the behaviors that matter most to your org.

**In essence, Energy Points turn mundane tasks into a game, making work more fun and driving the digital behavior that leads to real-world business success.**