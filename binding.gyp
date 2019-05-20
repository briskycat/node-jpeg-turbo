{
  'targets': [
    {
      'target_name': 'jpegturbo',
      'sources': [
        'src/buffersize.cc',
        'src/compress.cc',
        'src/decompress.cc',
        'src/exports.cc',
      ],
      'include_dirs': [
        '<!(node -e "require(\'nan\')")'
      ],
      'libraries': [ "-l:libjpeg.a" ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.9'
          },
          'include_dirs': [
            '/opt/local/include'
          ]
        }]
      ]
    }
  ]
}
