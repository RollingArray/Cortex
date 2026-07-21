"""
Cortex Command Line Interface

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides the command line interface for
Cortex administrative and developer
operations.

Features:
---------
- Database operations
- Data seeding
- Development utilities
"""

# =============================================================================
# Imports
# =============================================================================

import typer

from backend.commands.seed import (
    seed_command,
)

# =============================================================================
# CLI
# =============================================================================

app = typer.Typer(
    help="Cortex Command Line Interface",
)

# =============================================================================
# Commands
# =============================================================================

app.command(
    name="seed",
)(
    seed_command,
)

# =============================================================================
# Main
# =============================================================================

if __name__ == "__main__":

    app()
