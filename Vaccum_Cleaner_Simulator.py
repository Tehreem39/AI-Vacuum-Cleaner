import tkinter as tk
import time


class InteractiveVacuum:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 AI Vacuum Cleaner Simulator")

        # Grid state variables
        self.vacuum_x = 150  # Start position centered in Room A (X: 0 to 300)
        self.room_a_dirty = True
        self.room_b_dirty = True

        # 1. Setup Canvas Drawing Window
        self.canvas = tk.Canvas(root, width=600, height=400, bg="#f0f0f0")
        self.canvas.pack() # Display window

        # 2. Draw Environment Layout
        self.draw_environment()

        # 3. Start the AI Animation Loop
        self.root.after(1000, self.run_ai_loop)

    def draw_environment(self):
        self.canvas.delete("all")  # Wipe screen clean for next frame

        # Draw Room A background box
        color_a = "#b49696" if self.room_a_dirty else "#ccffcc"
        self.canvas.create_rectangle(0, 0, 300, 400, fill=color_a, outline="#999999", width=3)
        self.canvas.create_text(150, 40, text="ROOM A", font=("Arial", 16, "bold"), fill="#333333")
        status_a = "🗑️🗑️🗑️🗑️ DIRTY" if self.room_a_dirty else "✨ CLEAN"
        self.canvas.create_text(150, 70, text=status_a, font=("Arial", 14), fill="#555555")

        # Draw Room B background box
        color_b = "#9B7E7E" if self.room_b_dirty else "#ccffcc"
        self.canvas.create_rectangle(300, 0, 600, 400, fill=color_b, outline="#999999", width=3)
        self.canvas.create_text(450, 40, text="ROOM B", font=("Arial", 16, "bold"), fill="#333333")
        status_b = "🗑️🗑️🗑️🗑️ DIRTY" if self.room_b_dirty else "✨ CLEAN"
        self.canvas.create_text(450, 70, text=status_b, font=("Arial", 14), fill="#555555")

        # Draw the Vacuum Cleaner Agent (Red Circle)
        self.canvas.create_oval(self.vacuum_x - 35, 200 - 35, self.vacuum_x + 35, 200 + 35, fill="#cc0000",
                                outline="#660000", width=2)
        self.canvas.create_text(self.vacuum_x, 200, text="🤖", font=("Arial", 20))

    def move_to(self, target_x):
        """Animates the vacuum sliding pixel-by-pixel across the screen"""
        step = 5 if target_x > self.vacuum_x else -5
        while self.vacuum_x != target_x:
            self.vacuum_x += step
            self.draw_environment()
            self.root.update()
            time.sleep(0.01)  # Control moving velocity smoothness

    def run_ai_loop(self):
        # Action Step 1: Clean Room A if vacuum is in Room A and it's dirty
        if self.vacuum_x == 150 and self.room_a_dirty:
            time.sleep(0.5)  # Pause to simulate sucking dirt
            self.room_a_dirty = False
            self.draw_environment()

        # Action Step 2: If Room A is clean but Room B is dirty, move right
        elif self.vacuum_x == 150 and self.room_b_dirty:
            time.sleep(0.5)
            self.move_to(450)  # Move to Room B tracking coordinates

        # Action Step 3: Clean Room B if vacuum is in Room B and it's dirty
        elif self.vacuum_x == 450 and self.room_b_dirty:
            time.sleep(0.5)
            self.room_b_dirty = False
            self.draw_environment()

        # Action Step 4: If everything is clean, return back home to A
        elif not self.room_a_dirty and not self.room_b_dirty and self.vacuum_x == 450:
            time.sleep(0.8)
            self.move_to(150)
            print("🎉 Execution Finished: All rooms are clean!")
            return  # Stop the loop execution safely

        # Keep checking status loops every half second
        self.root.after(500, self.run_ai_loop)


# Main script initialization root engine
if __name__ == "__main__":
    window = tk.Tk()
    app = InteractiveVacuum(window)
    window.mainloop()


