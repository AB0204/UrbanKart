# Deploy AB'Mart to Vercel

## Quick Deploy (Recommended)

1. **Install Vercel CLI** (if not already installed):
   ```bash
   npm install -g vercel
   ```

2. **Navigate to frontend directory**:
   ```bash
   cd /Users/abhiabhardwaj/.gemini/antigravity/playground/ecliptic-hawking/ecommerce-management-system/frontend
   ```

3. **Deploy to Vercel**:
   ```bash
   vercel
   ```
   
   Follow the prompts:
   - "Set up and deploy?"  → **Yes**
   - "Which scope?" → Choose your account
   - "Link to existing project?" → **No**
   - "Project name?" → **abmart** (or your preferred name)
   - "Directory?" → **./Frontend** (it will auto-detect)
   - "Override settings?" → **No**

4. **Production deployment**:
   ```bash
   vercel --prod
   ```

## Alternative: Deploy via GitHub + Vercel Dashboard

1. Push code to GitHub (if not done):
   ```bash
   cd /Users/abhiabhardwaj/.gemini/antigravity/playground/ecliptic-hawking/ecommerce-management-system
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository
5. Configure:
   - **Root Directory**: `frontend`
   - **Framework Preset**: Vite
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
6. Click "Deploy"

## Post-Deployment

Your AB'Mart store will be live at:
- `https://your-project-name.vercel.app`

The store will work with the mock data (35 products) without needing MySQL!

## Notes

- The deployed version uses mock product data
- Backend is not deployed (runs locally for now)
- To deploy backend, use Railway, Render, or similar services
- Free tier on Vercel is perfect for this project
