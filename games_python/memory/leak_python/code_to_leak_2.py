import leak_tracer

# Start memory tracing
leak_tracer.start_memory_trace()

# Your code

# Stop memory tracing
leak_tracer.stop_memory_trace()

# Display memory trace
leak_tracer.memory_leak_check()