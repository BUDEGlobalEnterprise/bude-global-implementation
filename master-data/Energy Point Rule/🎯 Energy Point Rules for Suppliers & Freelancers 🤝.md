# 🎯 Energy Point Rules for Suppliers & Freelancers 🤝

**Goal:** Build stronger relationships, improve performance, and create a fun, collaborative environment.

---

## 🏆 Supplier Performance & Partnership Tiers

### ⚡ **Platinum Partner Tier** (Top 1%)
*   **Unlocks:** Priority in RFP (Request for Proposal) opportunities, "Featured Supplier" status on our portal, quarterly business review with leadership.
*   **Rules:**
    *   `🚀 On-Time Delivery Streak`: +15 points for every 5 consecutive orders delivered **early** or **on-time**.
    *   `💎 Zero Defect Order`: +25 points for a large shipment (>100 units) with a **perfect quality check**.
    *   `📈 Cost-Saving Idea`: +50 points for a suggested process improvement that saves significant costs.

### ⚡ **Gold Partner Tier** (Top 10%)
*   **Unlocks:** Faster payment terms (Net 15), access to higher-value projects.
*   **Rules:**
    *   `⭐ Perfect Quality Score`: +10 points for an order that passes all quality checks on the first try.
    *   `🤝 Proactive Communication`: +5 points for proactively updating us on an order status (e.g., shipping delay) **before we have to ask**.
    *   `📊 ESG Champion`: +15 points for providing sustainability reports or carbon footprint data for their products.

### ⚡ **Silver Partner Tier** (Reliable)
*   **Unlocks:** Standard reliable partner status.
*   **Rules:**
    *   `✅ On-Time Delivery`: +5 points for delivering an order on the promised date.
    *   `📄 Documentation Star`: +3 points for submitting all required documents (e.g., invoices, packing lists, certifications) correctly on the first try.

---

## 🎨 Freelancer & Contractor Performance Tiers

### ✨ **A-List Freelancer Tier** (Elite)
*   **Unlocks:** First pick on high-budget projects, retainer agreements, "Top Freelancer" badge.
*   **Rules:**
    *   `🔥 Early Delivery`: +20 points for delivering a project **ahead of schedule**.
    *   `💡 Innovation Bonus`: +30 points for suggesting a creative solution that significantly improves the project outcome.
    *   `🎖️ Client Rave Review`: +40 points for receiving unsolicited, glowing feedback from an internal stakeholder.

### ✨ **Rockstar Freelancer Tier** (Consistently Great)
*   **Unlocks:** Access to more complex projects, higher rate negotiations.
*   **Rules:**
    *   `⚡ Zero Revision Project`: +15 points for delivering work that requires **no revisions** and meets all brief requirements.
    *   `📊 Meticulous Reporting`: +10 points for providing clear, concise, and timely progress updates without being reminded.
    *   `🛠️ Tool Mastery`: +5 points for expertly using our project management/ collaboration tools (e.g., completes profile, uses correct statuses).

### ✨ **Rising Star Tier** (New & Promising)
*   **Unlocks:** More opportunities, mentorship from a project lead.
*   **Rules:**
    *   `🚀 First Project Success`: +25 points for successfully completing their first project with us.
    *   `📚 Quick Learner`: +10 points for quickly getting up to speed with our brand guidelines and processes.
    *   `🤔 Great Questions`: +5 points for asking insightful questions that clarify the project brief and prevent misunderstandings.

---

## 🏅 Special Badges & One-Time Bonuses (For All)

| Badge & Emoji | How to Earn It | Points |
| :--- | :--- | :--- |
| **`🎯 First Order`** | Successfully complete your first ever transaction with us. | `+10` |
| **`📈 Growth Partner`** | Increase your business volume with us by 20% quarter-over-quarter. | `+50` |
| **`❤️ Culture Fit`** | Your team's values and communication style align perfectly with ours. | `+25` |
| **`⚡ Emergency Hero`** | Help us out of a jam with a last-minute, urgent request. | `+35` |
| **`🦉 Owl Award`** | Provide exceptional work or support outside of standard business hours. | `+15` |
| **`🔗 Referral Guru`** | Refer another high-quality supplier or freelancer that we end up hiring. | `+30` |

---

## 🔧 How to Implement This in ERPNext

1.  **For Suppliers:** Most rules would be based on the **`Purchase Order`**, **`Purchase Receipt`**, and **`Quality Inspection`** doctypes.
    *   *Example Rule for "On-Time Delivery":*
    *   **Document:** `Purchase Receipt`
    *   **Event:** `Submit`
    *   **Condition:** `doc.schedule_date >= doc.posting_date` (Received on or before scheduled date)
    *   **Points:** `+5` to the **Supplier's Contact** (linked user)

2.  **For Freelancers:** Base rules on the **`Project`**, **`Task`**, and **`Timesheet`** doctypes.
    *   *Example Rule for "Zero Revision Project":*
    *   **Document:** `Project`
    *   **Event:** `Value Change` (of status)
    *   **Condition:** `doc.status == "Completed" && doc.actual_end_date <= doc.expected_end_date`
    *   **Points:** `+15` to the **`project_manager`** (the freelancer)

**Pro Tip:** Create a **Portal Page** where your suppliers and freelancers can see their own points, tier, and badges! This transparency turns the system into a true engagement tool.