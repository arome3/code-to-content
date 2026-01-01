# MCP Server Integration Guide

This skill supports optional integration with MCP (Model Context Protocol) servers for direct social media posting. When no MCP server is available, content is delivered in copy-ready format.

---

## How MCP Integration Works

MCP servers extend Claude's capabilities by providing access to external services. When a compatible social media MCP server is configured, this skill can:

1. Generate content as usual (following all quality gates)
2. Detect available MCP tools
3. Offer direct posting option
4. Execute posting via MCP if approved
5. Return post URL/confirmation

---

## Supported MCP Servers

### Twitter/X Integration

**Expected MCP tool names:**
- `mcp__twitter__post_tweet` or `mcp__x__post_tweet`
- `mcp__twitter__create_thread` or `mcp__x__create_thread`

**When detected, offer:**
```
Content ready for Twitter. Would you like me to:
1. Post directly via MCP (requires approval)
2. Provide copy-ready format for manual posting
```

**Thread handling:**
- Split content at tweet boundaries
- Post first tweet, then replies in thread
- Return thread URL on completion

### LinkedIn Integration

**Expected MCP tool names:**
- `mcp__linkedin__create_post`
- `mcp__linkedin__share_article`

**When detected, offer:**
```
Content ready for LinkedIn. Would you like me to:
1. Post directly via MCP (requires approval)
2. Provide copy-ready format for manual posting
```

**Post handling:**
- Include formatted text with line breaks
- Attach images if URLs provided
- Handle hashtags appropriately

### Buffer/Scheduling Integration

**Expected MCP tool names:**
- `mcp__buffer__schedule_post`
- `mcp__buffer__add_to_queue`

**When detected, offer scheduling options:**
```
Content ready. Would you like me to:
1. Post now via MCP
2. Schedule for optimal time via Buffer
3. Provide copy-ready format for manual posting
```

---

## Detection Protocol

Before Phase 5 (Delivery), check for available MCP tools:

```
If any social MCP tools are available:
    1. Inform user: "I detected [platform] MCP integration"
    2. Offer posting options
    3. If user approves: execute MCP tool
    4. Return confirmation with post URL
Else:
    1. Deliver in copy-ready format
    2. Include platform-specific instructions
```

---

## Fallback: Copy-Ready Output

When no MCP server is available, always provide content in this format:

### Twitter Thread Format

```
═══════════════════════════════════════════════════════
COPY BELOW FOR TWITTER
═══════════════════════════════════════════════════════

[Tweet 1 - Hook]
Your hook text here (max 280 chars)

---

[Tweet 2]
Second tweet content here

---

[Tweet 3]
Third tweet content here

---

[Final Tweet - CTA]
Call to action with link

═══════════════════════════════════════════════════════

Character counts:
• Tweet 1: 142/280 ✓
• Tweet 2: 267/280 ✓
• Tweet 3: 198/280 ✓
• Tweet 4: 89/280 ✓

Suggested images:
• Tweet 1: Hero image or result screenshot
• Tweet 5: Diagram or code snippet

Best posting times (engagement):
• Weekdays: 8-9am, 12-1pm, 5-6pm
• Weekends: 9-11am

📋 Posting instructions:
1. Copy each tweet individually
2. Post first tweet
3. Reply to create thread
4. Add images as noted
```

### LinkedIn Post Format

```
═══════════════════════════════════════════════════════
COPY BELOW FOR LINKEDIN
═══════════════════════════════════════════════════════

[Hook line 1 - visible before "see more"]
[Hook line 2 - visible before "see more"]

[Body paragraph 1]

[Body paragraph 2]

[Body paragraph 3]

Key takeaways:

• Takeaway 1
• Takeaway 2
• Takeaway 3

[Engagement question]

#hashtag1 #hashtag2 #hashtag3

═══════════════════════════════════════════════════════

Stats:
• Character count: 1,247/3,000 ✓
• Hook visibility: First 2 lines before "see more" ✓
• Hashtags: 3 (optimal: 3-5) ✓

Suggested image:
• Professional photo or diagram
• Aspect ratio: 1.91:1 (1200x628px) optimal

Best posting times (engagement):
• Tuesday-Thursday: 7-8am, 12pm, 5-6pm
• Avoid weekends for B2B content

📋 Posting instructions:
1. Copy entire post
2. Add line breaks as shown (LinkedIn preserves them)
3. Add image before posting
4. Consider tagging relevant people/companies
```

---

## Future MCP Server Candidates

These MCP servers may become available for integration:

### Publishing Platforms
- `mcp__medium__publish_article`
- `mcp__devto__create_post`
- `mcp__hashnode__publish_article`
- `mcp__substack__create_post`

### Social Platforms
- `mcp__mastodon__post_toot`
- `mcp__bluesky__create_post`
- `mcp__threads__create_post`

### Content Management
- `mcp__notion__create_page`
- `mcp__wordpress__create_post`
- `mcp__ghost__publish_post`

### Scheduling
- `mcp__hootsuite__schedule_post`
- `mcp__later__add_to_queue`
- `mcp__sprout__create_post`

---

## User Approval Requirements

**Always require explicit user approval before:**
- Posting to any social platform
- Publishing to any blog/newsletter
- Scheduling any content

**Never auto-post without confirmation.** Even with MCP available, ask:
```
Ready to post to [Platform]. This will be visible to [audience estimate].

Proceed with posting? (yes/no)
```

---

## Error Handling

If MCP posting fails:
1. Capture error message
2. Fall back to copy-ready format
3. Report: "Posting failed: [reason]. Here's copy-ready content instead."

Common failure reasons:
- Authentication expired
- Rate limit reached
- Content policy violation
- Network timeout

---

## Configuration Notes

To enable MCP integration, users need to:

1. Install compatible MCP server (when available)
2. Configure authentication in MCP server settings
3. Add server to Claude Code MCP configuration:

```json
{
  "mcpServers": {
    "twitter": {
      "command": "npx",
      "args": ["-y", "@example/twitter-mcp-server"],
      "env": {
        "TWITTER_API_KEY": "...",
        "TWITTER_API_SECRET": "..."
      }
    }
  }
}
```

The skill will automatically detect available MCP tools and offer integration options.
