#!/usr/bin/env python3
"""
Unified CLI for relevance_connect package.
"""
import argparse
import sys
from relevance_connect.login import main as login_main
from relevance_connect.run import main as run_main


def main():
    parser = argparse.ArgumentParser(
        description='Relevance Connect CLI - Manage and run Relevance AI integrations',
        prog='relevance-connect'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Login subcommand
    login_parser = subparsers.add_parser('login', help='Authenticate with Relevance AI')
    login_parser.add_argument(
        'region', 
        type=str, 
        help='Region for authentication', 
        nargs='?',
        default=None
    )
    login_parser.add_argument(
        'api_key', 
        type=str, 
        help='API key for authentication', 
        nargs='?',
        default=None
    )
    
    # Run subcommand
    run_parser = subparsers.add_parser('run', help='Run a relevance_connect integration')
    run_parser.add_argument(
        '-m', '--main', 
        type=str, 
        help='Path to main.py file', 
        default='main.py'
    )
    run_parser.add_argument(
        '-mt', '--metadata', 
        type=str, 
        help='Path to metadata.json file', 
        default='metadata.json'
    )
    run_parser.add_argument(
        '-i', '--inputs', 
        type=str, 
        help='Path to inputs.json file', 
        default='inputs.json'
    )
    
    args = parser.parse_args()
    
    if args.command == 'login':
        # Call login with the appropriate arguments
        sys.argv = ['login']
        if args.region:
            sys.argv.append(args.region)
        if args.api_key:
            sys.argv.append(args.api_key)
        login_main()
    elif args.command == 'run':
        # Call run with the appropriate arguments
        sys.argv = ['run', '-m', args.main, '-mt', args.metadata, '-i', args.inputs]
        run_main()
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()