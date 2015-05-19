# -*- mode: python -*-
a = Analysis(['convert.py'],
             pathex=['g:\\MaguMemo\\MagnaMemoria_dev\\tools\\WebContent\\sol'],
             hiddenimports=['gfm', 'mdx_gfm'],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='convert.exe',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='convert')
