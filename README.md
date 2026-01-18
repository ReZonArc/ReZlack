# ReZlack

A repository-based Slack workspace representation, mapping Slack workspace structure to files and folders.

## Workspace Structure

The `workspace/` directory contains a file-based representation of a Slack workspace:

- **channels/** - Public and private channels with messages
- **users/** - User profiles and information
- **direct-messages/** - Direct message conversations
- **threads/** - Message threads and replies

See [workspace/README.md](workspace/README.md) for detailed documentation.

## Testing

Run tests with:
```bash
python test.py
```