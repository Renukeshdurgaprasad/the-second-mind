class ProximityAgent:
    def process(self, refined_hypothesis, memory):
        past_data = memory.retrieve("solar")
        return refined_hypothesis + f" (Learned: {past_data})" if past_data else refined_hypothesis
