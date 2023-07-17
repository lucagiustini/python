import memory_tracer
import gc

# Start memory tracing
memory_tracer.start_memory_trace()

# Your code

gc.collect()


# Stop memory tracing
memory_tracer.stop_memory_trace()

# Display memory trace
memory_tracer.display_memory_trace()