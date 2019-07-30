class GameStats():
    """Track statistics for alien Invasion"""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_status()

    def reset_status(self):
        """Initialize statistcs that can change through the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.game_active = True