guard 'nosetests', cli: '--verbose' do
  watch(%r{^tests/(.*)/?test_(.*)\.py$})
  watch(%r{^(.*)/(.*)\.py$}) do |matches|
    "tests/test_#{matches[2]}.py"
  end
end
