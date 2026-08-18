import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const supabaseUrl = "https://zuptxhcjzhqynrquyray.supabase.co";

const supabaseKey = "sb_publishable_1sa0MtE83MZXETR5JLakJA_fRVrjDJI";

export const supabase = createClient(
  supabaseUrl,
  supabaseKey
);
