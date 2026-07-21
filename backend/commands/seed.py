"""
Seed Command

Author:
-------
Ranjoy Sen

Purpose:
--------
Provides database seeding commands for
the Cortex platform.

Features:
---------
- Seed default Workspace
"""

# =============================================================================
# Imports
# =============================================================================

import typer

from backend.seeders.workspace import (
    seed_workspace,
)

# =============================================================================
# Command
# =============================================================================


def seed_command() -> None:
    """
    Seed the Cortex database.
    """

    typer.echo()

    typer.echo(
        "Seeding Cortex database...",
    )

    typer.echo()

    seed_workspace()

    typer.echo()

    typer.echo(
        "Database seeding completed successfully.",
    )
