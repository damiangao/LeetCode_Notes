# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a personal LeetCode problem solutions repository. Each file is named with a LeetCode problem number followed by a dot (e.g., `1.`, `17.`, `1614.`) and contains Python code with one or more solution approaches.

## Code Structure

- Each numbered file contains a `Solution` class with the relevant method(s) for that problem
- Solutions use type hints and docstrings following LeetCode's format
- Multiple solution variants (naive, elegant, optimized) may be present in a single file

## No Build/Test System

This is a study/reference repository with no:
- Build commands
- Test suite
- Linting configuration
- Package dependencies

## Working with Solutions

When adding or modifying solutions:
- Follow the existing file naming convention (problem number + dot)
- Include type hints on method signatures
- Use List from typing for type annotations
- Keep docstrings in LeetCode's `:type:` and `:rtype:` format for compatibility
