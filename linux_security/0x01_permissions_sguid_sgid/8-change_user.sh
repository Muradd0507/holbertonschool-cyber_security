#!/bin/bash
find $1 -type f -exec chown -user user2 user3 {}\;
