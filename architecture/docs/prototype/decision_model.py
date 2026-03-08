class Decision:

    def _init_(self, context, options):
        self.context = context
        self.options = options
        self.selected_option = None

    def evaluate(self):
        print("Evaluating decision options...")
        for option in self.options:
            print("Option:", option)

    def select(self, option):
        if option in self.options:
            self.selected_option = option
            print("Decision selected:", option)
        else:
            print("Invalid option")

    def record_outcome(self):
        print("Decision outcome recorded for:", self.selected_option)


if _name_ == "_main_":

    context = "Select cloud provider"

    options = ["AWS", "Azure", "GCP"]

    decision = Decision(context, options)

    decision.evaluate()

    decision.select("Azure")

    decision.record_outcome()
