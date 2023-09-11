#include "benchmark/benchmark.h
#include "gtest/gtest.hstatic void BM_StringCreation(benchmark::State& state) {
for (auto _ : state)
	std::string empty_string;
}
// Register the function as a benchmark
BENCHMARK(BM_StringCreation);

// Define another benchmark
static void BM_StringCopy(benchmark::State& state) {
std::string x = "hello";
for (auto _ : state)
	std::string copy(x);
}
BENCHMARK(BM_StringCopy);
int main(int argc, char **argv) {
	::benchmark::RunSpecifiedBenchmarks();
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}
