# Steward's notebook

## Private handoff

Intended remote: https://github.com/unfinished-intelligence/garden. Sarasha administers the organization. Select Private on creation. Grant the GitHub app access to this repository only. Confirm private visibility and the destination owner before transferring. If the remote already contains work, inspect and integrate it on a branch. Never force-push the founding snapshot over another history.

## Keeping a recoverable archive

After significant changes, review the diff, update provenance, run the build, and check that only intended files changed. Check the page on a narrow screen, with keyboard navigation, enlarged text and dark mode. Give future images meaningful alternatives or mark decorative images accordingly. Review access when contributors change. Keep account recovery materials in the steward's password manager. Keep tokens, private correspondence, personal research records and registrar exports outside Git.

After committing, run `git bundle create ../garden.bundle --all` and `git bundle verify ../garden.bundle`. Keep a separate access-controlled copy. Restore to a fresh directory with `git clone -b main ../garden.bundle restored-garden`. Compare the commit ID with the source, rebuild and check the working tree. Bundles include committed Git history only. Maintain registrar recovery separately. Review access, backups and restore readiness quarterly or after a stewardship handover.

## Domain worksheet for a public edition

The registered domain is unfinishedintelligence.org. The steward's existing contact address is unfinishedintelligence@gmail.com. Do not alter mail or nameserver settings for a website cutover.

GitHub Free for organizations supports Pages from public repositories. Leave the archive private. For a future zero-cost release, use a separate public repository named unfinished-intelligence.github.io, containing only reviewed site/index.html and site/garden.css at its root. Review the actual export files and start with fresh public history. No deploy workflow is necessary.

1. The publishing contributor selects and reviews the public files under [Directive 002](../governance/founding-autonomy-directive-002.md). Verify the domain in the organization's Pages settings by adding the GitHub-issued TXT record at its specified host. Keep that record.
2. Take a private snapshot of existing DNS records and identify conflicting apex or www web records and any existing service before replacing them.
3. Configure branch-based Pages hosting for the reviewed public export. Set its custom domain to unfinishedintelligence.org before pointing traffic at GitHub. ops/CNAME.example is the proposed content of the publishing root's CNAME file.
4. At the authoritative DNS provider set apex @ ALIAS/ANAME to unfinished-intelligence.github.io if supported. Alternatively use four apex A records: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153. Set www CNAME to unfinished-intelligence.github.io. Recheck live GitHub documentation at cutover. Avoid wildcard records.
5. Verify the apex and www resolution, certificate and canonical redirect. Enable Enforce HTTPS when the certificate is ready. If rolling back, first restore prior DNS and allow cached records to expire before releasing the Pages domain binding.

Provider, current zone, account plan and certificate status have not been inspected. The worksheet is inert.

Sources: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages and https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
