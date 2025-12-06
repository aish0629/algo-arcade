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
