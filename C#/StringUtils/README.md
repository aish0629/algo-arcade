# C# String Utilities

This folder contains a small .NET console project demonstrating string/array utilities ported from JS/Python implementations. It also includes an xUnit test project that mirrors the Python/xUnit test coverage.

## Project structure

```
C#/StringUtils/
├── StringUtils.csproj
├── StringUtilities.cs        # utility methods (namespace: AlgoArcade.Strings)
├── Program.cs                # runner demonstrating positive/negative scenarios
├── README.md                 # this file
└── ../StringUtils.Tests/     # xUnit test project (sibling folder)
    ├── StringUtils.Tests.csproj
    └── StringUtilitiesTests.cs
```

## Requirements

- .NET SDK 6.0 or 7.0 installed (tested with .NET 7). Use `dotnet --info` to verify your SDK.

## Run the runner (console demo)

Open PowerShell in this folder and run:

```powershell
cd "d:\src\playwright\Aishwarya\Aish First Plywright\algo-arcade\C#\StringUtils"
dotnet run --project StringUtils.csproj
```

This prints positive and negative scenario outputs for each utility to the console.

## Run tests (xUnit)

An xUnit test project `StringUtils.Tests` was added to mirror the Python tests. To run the tests:

```powershell
cd "d:\src\playwright\Aishwarya\Aish First Plywright\algo-arcade\C#\StringUtils.Tests"
dotnet test
```

Common options:
- Run tests with detailed verbosity:

```powershell
dotnet test -v normal
```

- Run a specific test (use `--filter`):

```powershell
dotnet test --filter FullyQualifiedName~AlgoArcade.Strings.Tests.ReverseStringTests.NormalString
```

## Notes

- Methods are implemented in `AlgoArcade.Strings.StringUtilities` and are null-safe to mirror the original JS/Python behavior. Examples include `ReverseString`, `IsPalindrome`, `CharFrequency`, `RemoveDuplicatesFromArray`, `SecondLargest`, `IsNumeric`, `ReverseWords`, `FirstNonRepeatingChar`, `SumArray`, and `HasDuplicates`.
- The test project references the main project via a project reference; ensure the sibling folder `StringUtils` is present relative to `StringUtils.Tests`.
- Tests target `net7.0`. If you prefer `net6.0` or another framework, I can update both csproj files.

## Test results (local)

- All xUnit tests were executed locally and passed (49 tests). You can reproduce by running `dotnet test` as shown above.

## Next steps (optional)

- Add GitHub Actions workflow to run `dotnet test` on push/PR.
- Add an NUnit alternative or extend tests to cover additional edge cases (Unicode, huge inputs).

If you want, I can add CI workflow and a `README` badge showing test status.
# C# String Utilities

This folder contains a small .NET console project demonstrating string/array utilities ported from JS/Python implementations.

## Project structure

```
C#/StringUtils/
├── StringUtils.csproj
├── StringUtilities.cs   # utility methods
├── Program.cs           # runner demonstrating positive/negative scenarios
└── README.md
```

## Requirements
- .NET SDK 6.0 or 7.0 installed (tested with .NET 7)

## Run
Open PowerShell in this folder and run:

```powershell
dotnet run --project StringUtils.csproj
```

This prints positive and negative scenarios to the console.

## Notes
- Methods are in namespace `AlgoArcade.Strings` and class `StringUtilities`.
- Null inputs map to `null`/`false`/empty as appropriate to match the JS/Python behavior.
